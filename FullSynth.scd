// Configuración inicial del servidor
s.options.sampleRate = 48000;
s.reboot;

(
SynthDef(\synth, { |freq=440, ataque=0.1, decaimiento=1, gate=1, 
    delayAmount=0, distAmount=0, noiseAmount=0|
    var sig, env, delay, noise;
    
    // Oscilador base
    sig = SinOsc.ar(freq, 0, 0.5);
    
    // Envelope
    env = EnvGen.ar(Env.perc(ataque, decaimiento), gate, doneAction: 2);
    
    sig = sig * env;
    
    // Efectos
    delay = CombL.ar(sig, 0.5, 0.3, 2.0) * delayAmount;
    sig = sig + delay;
    
    sig = (sig * (1 + (distAmount * 10))).clip2(1);
    
    noise = WhiteNoise.ar(noiseAmount);
    sig = sig + noise;
    
    Out.ar(0, sig!2);
}).add;

// Variable global para almacenar synths activos
~activeSynths = List[];

OSCdef(\recibirFrecuencias, { |msg|
    var modo = msg[1];
    var frecuencias = msg[2..msg.size-6];
    var ataque = msg[msg.size-5];
    var decaimiento = msg[msg.size-4];
    var efectos = msg[msg.size-3..msg.size-1];
    
    // Limpiar synths anteriores de manera segura
    ~activeSynths = ~activeSynths.select({ |synth| 
        if(synth.isPlaying) {
            synth.set(\gate, 0);
            true
        } {
            false
        }
    });
    
    if(modo == 'simultaneo', {
        frecuencias.do({ |freq|
            var synth = Synth(\synth, [
                \freq, freq,
                \ataque, ataque,
                \decaimiento, decaimiento,
                \delayAmount, efectos[0],
                \distAmount, efectos[1],
                \noiseAmount, efectos[2],
                \gate, 1
            ]);
            ~activeSynths.add(synth);
        });
    }, {
        // Modo individual
        Routine({
            frecuencias.do({ |freq|
                var synth = Synth(\synth, [
                    \freq, freq,
                    \ataque, ataque,
                    \decaimiento, decaimiento,
                    \delayAmount, efectos[0],
                    \distAmount, efectos[1],
                    \noiseAmount, efectos[2],
                    \gate, 1
                ]);
                ~activeSynths.add(synth);
                (ataque + decaimiento + 0.1).wait;
            });
        }).play;
    });
}, '/frecuencia_palabra');

OSCdef(\stopAll, { |msg|
    // Detener todos los synths activos de manera segura
    ~activeSynths = ~activeSynths.select({ |synth| 
        if(synth.isPlaying) {
            synth.set(\gate, 0);
            true
        } {
            false
        }
    });
}, '/stop_all');
)
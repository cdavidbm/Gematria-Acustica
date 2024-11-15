// Configuración inicial del servidor
s.options.sampleRate = 48000;
s.reboot;

// OSCdef para reproducir frecuencias
(
OSCdef.new(
    \recibirFrecuencias,
    { |msg, time, addr, port|
        var modo = msg[1];
        var frecuencias = msg[2..msg.size-3];
        var ataque = msg[msg.size-2];
        var decaimiento = msg[msg.size-1];

        if(modo == 'simultaneo', {
            {
                Mix.new(
                    frecuencias.collect({ |freq|
                        var baseOsc = SinOsc.ar(freq, 0, 0.5);
                        var modOsc = SinOsc.ar(freq * 1.5, 0, 0.3);
                        var env = EnvGen.ar(Env.perc(ataque, decaimiento), doneAction: 2);
                        var filtro = LPF.ar(baseOsc * modOsc, freq * 4);
                        filtro * env;
                    })
                )
            }.play;
        }, {
            frecuencias.do({ |freq, i|
                var evt = SystemClock.sched(i * (ataque + decaimiento), {
                    {
                        var baseOsc = SinOsc.ar(freq, 0, 0.5);
                        var modOsc = SinOsc.ar(freq * 1.5, 0, 0.3);
                        var env = EnvGen.ar(Env.perc(ataque, decaimiento), doneAction: 2);
                        var filtro = LPF.ar(baseOsc * modOsc, freq * 4);
                        filtro * env;
                    }.play;
                    nil;
                });
            });
        });
    },
    '/frecuencia_palabra'
);
)
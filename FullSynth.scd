// Configuración inicial del servidor
s.options.sampleRate = 48000;
s.reboot;

~snt = NodeProxy.new;
~snt.fadeTime_(3);
~snt.play;

// OSCdef para recibir una lista de frecuencias y reproducirlas como un acorde
(
OSCdef.new(
    \recibirFrecuencias,
    { |msg, time, addr, port|
        var frecuencias = msg[1..msg.size-3]; // Obtener la lista de frecuencias
        var ataque = msg[msg.size-2];         // Obtener el tiempo de ataque
        var decaimiento = msg[msg.size-1];    // Obtener el tiempo de decaimiento
        
        ("Frecuencias recibidas: " ++ frecuencias).postln;
        ("Ataque: " ++ ataque ++ "s, Decaimiento: " ++ decaimiento ++ "s").postln;
        
        ~snt.source = {
            var baseOsc, modOsc, ringMod, env, filtro, ruido;
            Mix.new(
                baseOsc = SinOsc.ar(frecuencias, 0, 0.5);
                modOsc = SinOsc.ar(frecuencias * 1.5, 0, 0.3);
                ringMod = baseOsc * modOsc;
                // Usar los valores de ataque y decaimiento recibidos
                env = EnvGen.ar(Env.perc(ataque, decaimiento), doneAction: 2);
                ruido = LPF.ar(WhiteNoise.ar(0.07), frecuencias * 2);
                filtro = LPF.ar(ringMod + ruido, frecuencias * 4);
                filtro * env;
            )
        };
    },
    '/frecuencia_palabra' // Mensaje OSC para lista de frecuencias
);
)

// Para liberar el NodeProxy cuando sea necesario
~snt.release;

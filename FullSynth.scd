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
        var frecuencias = msg[1..]; // Obtener la lista de frecuencias desde Python
        ("Frecuencias recibidas: " ++ frecuencias).postln;

        ~snt.source = {
            var baseOsc, modOsc, ringMod, env, filtro, ruido;

            Mix.new(
                // Oscilador base (frecuencia principal)
                baseOsc = SinOsc.ar(frecuencias, 0, 0.5);

                // Oscilador modulador (para efectos de modulación en anillo)
                modOsc = SinOsc.ar(frecuencias * 1.5, 0, 0.3);

                // Modulación en anillo combinando el oscilador base y el modulador
                ringMod = baseOsc * modOsc;

                // Envolvente para dar forma al sonido con ataque y decaimiento
                env = EnvGen.ar(Env.perc(2, 1), doneAction: 2);

                // Ruido blanco filtrado para añadir textura al sonido
                ruido = LPF.ar(WhiteNoise.ar(0.07), frecuencias * 2);

                // Mezcla del sonido filtrado y modulado
                filtro = LPF.ar(ringMod + ruido, frecuencias * 4);

                // Aplicación final de la envolvente
                filtro * env;
            )
        };
    },
    '/frecuencia_palabra' // Mensaje OSC para lista de frecuencias
);
)

// Para liberar el NodeProxy cuando sea necesario
~snt.release;

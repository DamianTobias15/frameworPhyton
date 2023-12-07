// test_runner.js
import { exec } from 'child_process';

// Ejecuta las pruebas de Python
exec('python -m unittest discover tests', (err, stdout, stderr) => {
    console.log(stdout);
    console.error(stderr);
    if (err) {
        console.error(`Error ejecutando las pruebas de Python: ${err}`);
        process.exit(1);
    }

    // Puedes agregar aquí más pasos para ejecutar pruebas adicionales o realizar otras tareas.

    console.log('Pruebas completadas exitosamente.');
});

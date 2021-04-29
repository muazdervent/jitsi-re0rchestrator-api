const express = require('express');
const app = express();


const {spawn} = require('child_process');

app.get('/', (req, res) => {
 res.send('Merhaba Dünya!');
});



app.listen(3000, () => {
 console.log('Uygulama çalıştırıldı...');
});


app.get('/jitsi', (req, res) => {
    const operation = req.param('operation');
    const parameter = req.param('parameter');
    const parameter1 = req.param('parameter1');
	


    	var dataToSend;
    	// spawn new child process to call the python script
    	const python = spawn('python3', ['manage.py',operation,parameter,parameter1]);
    	// collect data from script
    	python.stdout.on('data', function (data) {
    	 console.log('Pipe data from python script ...');
    	 dataToSend = data.toString();
    	});
    	// in close event we are sure that stream from child process is closed
    	python.on('close', (code) => {
    	console.log(`child process close all stdio with code ${code}`);
    	// send data to browser
    	res.write(`${dataToSend}`);
    	//console.log(`datatosend : ${dataToSend}`);
    	res.end();
    	});



    //res.send(`${category} kategorisindeki ${titleUrl} içeriğine bakıyorsunuz.`);
});

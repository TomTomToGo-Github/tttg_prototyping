// 
const { exec } = require('child_process'); // ability to spawn child processes

// Create a JSON object with data from js to python
const data = {
    path: 'C:/Users/thoma/Desktop/Tommy/Programmieren/tttg_utils_js/prototyping',
    filename: 'hello_world.txt',
};

// Convert the JSON object to a string
const jsonData = JSON.stringify(data);
console.log('Data passed from JS to python: ', variablesString)
const subprogramString = 'python';
const scriptPathName = 'C:/Users/thoma/Desktop/Tommy/Programmieren/tttg_prototyping/word_button_python.py';
const commandString = `${subprogramString} ${scriptPathName} ${jsonData.replace(/'/g, '')}`;

// Run the Python script and return data from python to js using stdout
exec(commandString, (error, stdout, stderr) => {
        if (error) {
                console.error(`Error: ${error.message}`);
                return;
        }
        if (stderr) {
                console.error(`stderr: ${stderr}`);
                return;
        }
        console.log(`stdout: ${stdout}`);
        const regex = /{([^}]*)}/;
        const match = stdout.match(regex);
        const extractedData = match ? match[0] : null;
        console.log(extractedData);
        const receivedDataJson = JSON.parse(extractedData);
        console.log('Received json data:', receivedDataJson);
        console.log('Received field "content":', receivedDataJson['content']);
});


// // TUTORIAL DATA
// This is a single-line comment ONLY IN JS
// /*
// This is a
// multi-line comment ONLYIN JS
// */
// console.log('Hello World');
// let name = 'Mosh';
// console.log(name);

// // Cannot be a reserved keyword like if, else, let, etc.
// // Should be meaningful like name, age, etc.
// // Cannot start with a number (1name)
// // Cannot contain a space or hyphen (-)
// // Are case-sensitive (name, Name, NAME)
// // Use camel notation (firstName, lastName, etc.)

// // let firstName, lastName; // Declaring multiple variables possible but not best practice
// let firstName = 'Mosh' // Declare in separate lines
// let lastName = 'Hamedani'

// const interestRate = 0.3;
// // interestRate = 1; // error assignement to constant variable
// console.log(interestRate);



// // Write the JSON string to a file
// const fs = require('fs'); // node module to enable file system accesss
// fs.writeFile('data.json', jsonData, (err) => {
//     if (err) {
//         console.error(err);
//         return;
//     }
//     console.log('Data written to file successfully.');
// });


// // Read the JSON data from the file
// fs.readFile('data.json', 'utf8', (err, jsonString) => {
//     if (err) {
//         console.error(err);
//         return;
//     }
//     // Parse the JSON string back to an object
//     const receivedData = JSON.parse(jsonString);
//     console.log('Received data:', receivedData);
// });


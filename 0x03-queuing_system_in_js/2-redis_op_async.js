import { createClient } from 'redis';

const util = require('util');
const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${ err }`));

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, data) => {
    console.log(`Response: ${data}`);
  });
}

async function displaySchoolValue(schoolName) {
  let get = util.promisify(client.get).bind(client);
  let data = await get(schoolName);
  console.log(data);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

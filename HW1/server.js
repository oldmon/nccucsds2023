const dgram = require('dgram');

const server = dgram.createSocket('udp4');
server.on('message', (msg, rinfo) => {
  console.log(msg);
  const port = rinfo.port;
  server.send(`${port}:${msg}`,rinfo.port,rinfo.address, () => {
    server.close();
  });
});

server.on('error', (err) => {
  console.log(err);
});

// Listen port on 20213
server.bind(20213);

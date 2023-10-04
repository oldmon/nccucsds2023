const net = require("net");

const server = net.createServer((socket) => {
  // 當收到訊息時
  socket.on("message", (data) => {
    // 在 console 中印出所接收到的訊息
    console.log(data);

    // 取得 Client 的 port number
    const port = socket.remotePort;

    // 將收到的訊息的最前面加上「XXXX:」再送回給 Client
    socket.send(`XXXX:${data}`, () => {
      // 立即關閉連線
      socket.close();
    });
  });
});

// 傾聽本地端的 port 20213
server.listen(20213);


const ws = new WebSocket("ws://localhost:8000/voice")

function start(){

navigator.mediaDevices.getUserMedia({audio:true})

.then(stream => {

const recorder = new MediaRecorder(stream)

recorder.ondataavailable = e => {

ws.send(e.data)

}

recorder.start(1000)

})
}

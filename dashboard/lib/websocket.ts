export function connectTitanSocket(
    callback:any
){


    const socket =
    new WebSocket(
        "ws://localhost:8000/ws"
    )


    socket.onmessage = (
        event
    )=>{


        const data =
        JSON.parse(
            event.data
        )


        callback(
            data
        )


    }



    return socket

}

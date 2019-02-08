let events = {}

export const emit = (event, ...args) =>
  events[event].forEach(func => func(...args))

// Mock server emit
export const serverSocket = { emit }

// Mock socketIO connection
export const io = {
  connect() {
    return {
      on(event = [], func = () => null) {
        return new Promise(resolve => {
          const data = events[event]
            ? events[event].push(func)
            : (events[event] = [func])
          resolve(data)
        })
      },
      emit
    }
  }
}

export const socket = io.connect()

// Mock response socket
export const wsConnect = async () => {
  try {
    const res = await socket.on('connect', data => data)
    return res
  } catch (err) {
    throw Error(`Error connecting to ws: ${err}`)
  }
}

import io from 'socket.io-client'

export const socket = io()

export const wsConnect = async () => {
  try {
    const res = await socket.on('connect', data => data)
    return res
  } catch (err) {
    throw Error(`Error connecting to ws: ${err}`)
  }
}

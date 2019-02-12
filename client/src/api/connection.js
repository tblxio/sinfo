import io from 'socket.io-client'

export default {
  async wsConnect() {
    try {
      const socket = io()
      const res = await socket.on('connect', data => data)
      return res
    } catch (err) {
      throw Error(`Error connecting to ws: ${err}`)
    }
  }
}

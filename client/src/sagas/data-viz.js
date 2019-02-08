import { takeLatest, put, call, cancelled, take } from 'redux-saga/effects'
import { eventChannel } from 'redux-saga'
import { WATCH_DATA, ON_WATCH_DATA } from '../duxs/data-viz'

import { wsConnect } from '../api/connection'

export const createSocketChannel = (socket = {}) =>
  eventChannel(emit => {
    const handler = data => emit(data)
    socket.on('response', handler)
    return () => socket.off('response', handler)
  })

export function* watchData() {
  const socket = yield call(wsConnect)
  const socketChannel = yield call(createSocketChannel, socket)

  while (true) {
    try {
      const data = yield take(socketChannel)
      yield put({ type: ON_WATCH_DATA, payload: { data, connected: true } })
    } catch (err) {
      if (yield cancelled()) {
        socketChannel.disconnect()
      }
      throw Error(`there seems to be an error:  ${err}`)
    }
  }
}

export default function* dataVizSaga() {
  yield takeLatest(WATCH_DATA, watchData)
}

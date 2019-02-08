import { spawn, call, all } from 'redux-saga/effects'
import dataVizSaga from './data-viz'

function makeRestartable(saga) {
  return function*() {
    while (true) {
      try {
        yield call(saga)
        throw new Error(`unexpected root saga termination - ${saga}`)
      } catch (err) {
        throw err
      }
    }
  }
}

const rootSagas = [dataVizSaga].filter(s => s).map(makeRestartable)

export default function* rootSaga() {
  yield all(rootSagas.map(saga => spawn(saga)))
}

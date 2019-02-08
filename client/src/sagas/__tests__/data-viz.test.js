import { takeLatest } from 'redux-saga/effects'
import { testSaga } from 'redux-saga-test-plan'
import dataVizSaga, { watchData, createSocketChannel } from '../data-viz'
import { WATCH_DATA } from '../../duxs/data-viz'

import { wsConnect } from '../../api/connection'

jest.mock('../../api/connection', () => ({
  wsConnect: jest.fn()
}))

describe('saga data viz', () => {
  let generator = null
  beforeAll(() => {
    generator = dataVizSaga()
  })

  it('should run saga with takeLatest', () => {
    const expected = takeLatest(WATCH_DATA, watchData)
    const actual = generator.next().value
    expect(actual).toEqual(expected)
  })

  it('should run saga with call and put payload data from the socket', () => {
    const socket = wsConnect()
    let saga = testSaga(watchData)
    saga
      .next()
      .call(wsConnect)
      .next()
      .call(createSocketChannel, socket)
  })
})

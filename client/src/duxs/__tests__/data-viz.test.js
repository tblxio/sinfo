import reducer, { WATCH_DATA, ON_WATCH_DATA, watchData } from '../data-viz'

const initialState = {
  connected: false,
  data: {
    accelerometer: [],
    gyroscope: []
  },
  isLoading: false
}

const samplePayload = {
  connected: true,
  data: { accelerometer: [], gyroscope: [] }
}

// Test data viz output state
describe('data viz reducer', () => {
  it('should return the initial state', () => {
    expect(reducer(undefined, {})).toEqual({
      ...initialState
    })
  })

  it('should return the new state after WATCH_DATA action', () => {
    expect(
      reducer(initialState, {
        type: WATCH_DATA
      })
    ).toEqual({
      ...initialState,
      isLoading: true
    })
  })

  it('should return the new state after ON_WATCH_DATA action', () => {
    expect(
      reducer(initialState, {
        type: ON_WATCH_DATA,
        payload: {
          connected: true,
          data: {}
        }
      })
    ).toEqual({
      ...initialState,
      connected: samplePayload.connected,
      data: samplePayload.data,
      isLoading: false
    })
  })
})

// Test data viz action creators output action
describe('data viz actions', () => {
  it('should return the expected WATCH_DATA action', () => {
    expect(watchData()).toEqual({
      type: WATCH_DATA
    })
  })
})

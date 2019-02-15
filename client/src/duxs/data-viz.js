export const WATCH_DATA = 'WATCH_DATA'
export const ON_WATCH_DATA = 'ON_WATCH_DATA'

const initialState = {
  connected: false,
  data: {
    accelerometer: [],
    gyroscope: [],
    harshAccel: false,
    harshTurn: false,
    harshBumps: false
  },
  isLoading: false
}

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case WATCH_DATA: {
      return {
        ...state,
        isLoading: true
      }
    }
    case ON_WATCH_DATA: {
      const { data, connected } = action.payload

      return {
        ...state,
        connected,
        data: {
          accelerometer: data[0]
            ? state.data.accelerometer.length >= 10
              ? [
                  ...state.data.accelerometer.filter((arr, i) => i !== 0),
                  data[0]
                ]
              : [...state.data.accelerometer, data[0]]
            : [...state.data.accelerometer],
          gyroscope: data[1]
            ? state.data.gyroscope.length >= 10
              ? [...state.data.gyroscope.filter((arr, i) => i !== 0), data[1]]
              : [...state.data.gyroscope, data[1]]
            : [...state.data.gyroscope],
          harshAccel: data[3] && parseInt(data[3]) > 0 ? true : false,
          harshTurn: data[4] && parseInt(data[4]) > 0 ? true : false,
          harshBumps: data[5] && parseInt(data[5]) > 0 ? true : false
        },
        isLoading: false
      }
    }
    default: {
      return state
    }
  }
}

export function watchData() {
  return {
    type: WATCH_DATA
  }
}

export const getData = state => state.dataViz.data
export const getStatus = state => state.dataViz.connected

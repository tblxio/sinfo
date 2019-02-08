export const WATCH_DATA = 'WATCH_DATA'
export const ON_WATCH_DATA = 'ON_WATCH_DATA'

const initialState = {
  connected: false,
  data: {},
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
        data: { ...data },
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

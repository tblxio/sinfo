import apiCaller from '../connection'

// Test For socketIO connection
describe('Testing ws: caller', () => {
  it('should resolve socket data', async () => {
    expect.assertions(1)
    const socket = apiCaller.wsConnect()
    expect(apiCaller.wsConnect()).toEqual(socket)
  })

  it('should fail with an error', async () => {
    try {
      await apiCaller.wsConnect()
    } catch (err) {
      expect(err).toMatch(`Error connecting to ws: ${err}`)
    }
  })
})

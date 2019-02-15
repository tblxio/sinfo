import React from 'react'
import { shape, bool, string } from 'prop-types'

const Signal = ({
  styles = {},
  text = 'Harsh acceleration',
  signal = false,
  iconType = 'accel'
}) => (
  <aside className="Signal" style={styles}>
    <div className="Signal-container">
      <h4 className="Signal-text">{text}</h4>
      {iconType === 'accel' ? (
        <svg
          width="79px"
          height="34px"
          viewBox="0 0 79 34"
          xmlns="http://www.w3.org/2000/svg"
          className="Signal-accel"
        >
          <g
            id="Page-1"
            stroke="none"
            strokeWidth="1"
            fill="none"
            fillRule="evenodd"
          >
            <g
              className={`Signal-icon ${signal ? 'Signal-icon--active' : ''}`}
              transform="translate(-1320.000000, -273.000000)"
            >
              <g id="Graphics" transform="translate(40.000000, 180.000000)">
                <g id="Alerts" transform="translate(1268.000000, 39.000000)">
                  <g
                    id="Icon_Acceleration_active"
                    transform="translate(8.000000, 50.000000)"
                  >
                    <g>
                      <g>
                        <path
                          d="M66.8220339,36.7586207 C57.8871899,36.7586207 50.6440678,29.4793883 50.6440678,20.5 C50.6440678,11.5206117 57.8871899,4.24137931 66.8220339,4.24137931 C75.7568779,4.24137931 83,11.5206117 83,20.5 C83,29.4793883 75.7568779,36.7586207 66.8220339,36.7586207 Z M66.8220339,31.5139043 C72.8746701,31.5139043 77.7813013,26.5828114 77.7813013,20.5 C77.7813013,14.4171886 72.8746701,9.48609566 66.8220339,9.48609566 C60.7693977,9.48609566 55.8627665,14.4171886 55.8627665,20.5 C55.8627665,26.5828114 60.7693977,31.5139043 66.8220339,31.5139043 Z"
                          id="Combined-Shape"
                        />
                        <path
                          d="M66.8220339,28.2758621 C62.5488477,28.2758621 59.0847458,24.79449 59.0847458,20.5 C59.0847458,16.20551 62.5488477,12.7241379 66.8220339,12.7241379 C71.0952201,12.7241379 74.559322,16.20551 74.559322,20.5 C74.559322,24.79449 71.0952201,28.2758621 66.8220339,28.2758621 Z M66.8220339,26.2022989 C69.9557038,26.2022989 72.4960452,23.6492927 72.4960452,20.5 C72.4960452,17.3507073 69.9557038,14.7977011 66.8220339,14.7977011 C63.688364,14.7977011 61.1480226,17.3507073 61.1480226,20.5 C61.1480226,23.6492927 63.688364,26.2022989 66.8220339,26.2022989 Z"
                          id="Combined-Shape"
                        />
                        <path
                          d="M47.1661447,10.9222083 C46.187319,10.8750278 45.045798,10.5842395 44.1397901,9.85109186 C38.5560993,5.33273149 35.6847108,8.81618318 27.9885772,8.11434193 C33.3726689,11.8725233 35.6863673,9.76996911 38.7336064,10.6714903 C42.8492258,11.8890904 42.8543374,14.8322233 39.809745,15.4512337 C37.8308221,15.8535779 31.6405143,14.0651475 27.9970917,13.0167461 C18.7482274,10.3553689 15.7160081,20.2611929 3.1000097,20.9051091 C12.8923635,25.0983746 16.6843324,17.742703 21.3696064,17.7508938 C24.3961289,17.7561849 27.1974913,19.5126828 27.2044399,23.5135068 C27.2108154,27.1843379 24.254876,30.2188755 18.3882275,27.9501929 C13.6040533,26.1001122 10.4963745,29.0673528 8.45515488,30.1912542 C18.3908272,29.4470151 17.3536873,33.5786902 21.829398,34.4508934 C26.3051086,35.3230965 32.4504461,32.8002082 35.032875,30.6489069 C36.8607558,29.1261844 40.8896828,27.1477261 46.6963089,29.0295221 C45.8199055,30.6792215 44.7811667,31.8038792 40.422467,32.8669446 C47.2757329,35.3597578 55.413868,30.5187981 57.2132533,28.2809512 C51.4652165,25.7357685 46.8998641,19.4291691 47.1661447,10.9222083 Z"
                          id="Path-5"
                          transform="translate(30.156631, 21.058398) rotate(14.000000) translate(-30.156631, -21.058398) "
                        />
                      </g>
                    </g>
                  </g>
                </g>
              </g>
            </g>
          </g>
        </svg>
      ) : iconType === 'turns' ? (
        <svg
          width="72px"
          height="41px"
          viewBox="0 0 72 41"
          xmlns="http://www.w3.org/2000/svg"
        >
          <g
            id="Page-1"
            stroke="none"
            strokeWidth="1"
            fill="none"
            fillRule="evenodd"
          >
            <g
              id="SINFO_Dashboard"
              transform="translate(-1324.000000, -450.000000)"
            >
              <g id="Graphics" transform="translate(40.000000, 180.000000)">
                <g id="Alerts" transform="translate(1268.000000, 39.000000)">
                  <g
                    id="Icon_Gyroscope"
                    transform="translate(16.000000, 231.000000)"
                  >
                    <g>
                      <g>
                        <g
                          id="Group-5"
                          transform="translate(15.428571, 0.000000)"
                          className={`Signal-icon ${
                            signal ? 'Signal-icon--active' : ''
                          }`}
                        >
                          <path
                            d="M20.5714286,41 C9.21014229,41 0,31.8218374 0,20.5 C0,9.17816263 9.21014229,0 20.5714286,0 C31.9327149,0 41.1428571,9.17816263 41.1428571,20.5 C41.1428571,31.8218374 31.9327149,41 20.5714286,41 Z M20.5714286,35.875 C29.0923933,35.875 36,28.991378 36,20.5 C36,12.008622 29.0923933,5.125 20.5714286,5.125 C12.0504639,5.125 5.14285714,12.008622 5.14285714,20.5 C5.14285714,28.991378 12.0504639,35.875 20.5714286,35.875 Z"
                            id="Combined-Shape"
                          />
                        </g>
                        <g
                          id="Group-4"
                          transform="translate(0.000000, 5.125000)"
                          className={`Signal-stroke ${
                            signal ? 'Signal-stroke--active' : ''
                          }`}
                        >
                          <path
                            d="M8.77997486,28.8928306 C2.70203809,22.4746406 3.52737291,8.69408508 8.77997486,2.27589512"
                            id="Path-7"
                          />
                          <polyline
                            id="Path-8"
                            transform="translate(6.179408, 5.872674) rotate(-9.000000) translate(-6.179408, -5.872674) "
                            points="10.6463937 10.039765 10.6419099 1.71037373 1.71242322 1.70558277"
                          />
                        </g>
                        <g
                          id="Group-4-Copy"
                          transform="translate(66.000000, 19.645833) scale(-1, -1) translate(-66.000000, -19.645833) translate(60.000000, 5.125000)"
                          className={`Signal-stroke ${
                            signal ? 'Signal-stroke--active' : ''
                          }`}
                        >
                          <path
                            d="M8.77997486,28.8928306 C2.70203809,22.4746406 3.52737291,8.69408508 8.77997486,2.27589512"
                            id="Path-7"
                          />
                          <polyline
                            id="Path-8"
                            transform="translate(6.179408, 5.872674) rotate(-9.000000) translate(-6.179408, -5.872674) "
                            points="10.6463937 10.039765 10.6419099 1.71037373 1.71242322 1.70558277"
                          />
                        </g>
                        <path
                          d="M21.2222377,12.7555556 C25.6301618,14.6175203 30.5560826,15.5485026 36,15.5485026 C41.4439174,15.5485026 46.2938058,14.6175203 50.5496652,12.7555556 L52.093192,16.7567647 C44.8978795,19.1311048 40.7075893,21.5087021 39.5223214,23.8895569 C38.3370536,26.2704116 37.7202846,30.7535354 37.6720145,37.3389282 L34.203683,37.3389282 C34.203683,30.6746487 33.6422991,26.1915249 32.5195312,23.8895569 C31.3967634,21.5875888 27.1499721,19.2099915 19.7791574,16.7567647 L21.2222377,12.7555556 Z"
                          id="Path-6"
                          className={`Signal-icon ${
                            signal ? 'Signal-icon--active' : ''
                          }`}
                        />
                      </g>
                    </g>
                  </g>
                </g>
              </g>
            </g>
          </g>
        </svg>
      ) : (
        <svg
          width="81px"
          height="41px"
          viewBox="0 0 81 41"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
        >
          <g
            id="Page-1"
            stroke="none"
            strokeWidth="1"
            fill="none"
            fillRule="evenodd"
          >
            <g
              id="SINFO_Dashboard"
              transform="translate(-1320.000000, -635.000000)"
              className={`Signal-icon ${signal ? 'Signal-icon--active' : ''}`}
            >
              <g id="Graphics" transform="translate(40.000000, 180.000000)">
                <g id="Alerts" transform="translate(1268.000000, 39.000000)">
                  <path
                    d="M52.2065542,448.999266 C57.1890541,448.923467 57.2210144,443 62.2162149,443 C67.2399332,443 67.2891516,448.952352 72.2541805,448.999906 C77.2985577,448.972551 77.3100441,443 82.3258978,443 C87.3532643,443 87.3989034,448.961001 92.374688,449 C92.374688,451.276042 92.374688,453.942708 92.374688,457 L72.265005,457 L52.265005,457 L32.1553221,457 L12,457 C12.004688,454.342403 12.004688,451.675737 12,449 C17.0791654,449 17.0791654,443 22.1065319,443 C27.1302502,443 27.1794687,448.952352 32.1444975,448.999906 C37.1888747,448.972551 37.2003612,443 42.2162149,443 C47.223819,443 47.2887847,448.914228 52.2065542,448.999266 Z M61.6715729,419.757359 L61.6715729,434.343146 L59.6715729,434.343146 L59.6715729,419.899495 L55.4142136,424.156854 L54,422.742641 L60.7426407,416 L67.4852814,422.742641 L66.0710678,424.156854 L61.6715729,419.757359 Z M43.6715729,430.585786 L48.0710678,426.186292 L49.4852814,427.600505 L42.7426407,434.343146 L36,427.600505 L37.4142136,426.186292 L41.6715729,430.443651 L41.6715729,416 L43.6715729,416 L43.6715729,430.585786 Z"
                    id="Icon_Bumps"
                  />
                </g>
              </g>
            </g>
          </g>
        </svg>
      )}
    </div>
  </aside>
)

Signal.propTypes = {
  styles: shape({}),
  text: string,
  signal: bool,
  iconType: string
}

export default Signal
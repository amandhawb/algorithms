// const axios = require('axios');

// function readApi() {
//     // API URL
//     const apiTestUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey=aba9ec363ad12a1bf31cd0afccc7';
//     const apiUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=aba9ec363ad12a1bf31cd0afccc7';
//     const api = IS_TEST_MODE ? apiTestUrl : apiUrl;

//     // Fetching the data from the API
//     axios.get(api)
//     .then(response => {
//         console.log('here', response.data)
//         // Handle the success and display the data
//         processInput(response.data.callRecords)
        
//     })
//     .catch(error => {
//         // Handle any errors
//         console.error('Error fetching data:', error);
//     });
// }

// function readAnswerApi() {
//     // API URL
//     const apiUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset-answer?userKey=aba9ec363ad12a1bf31cd0afccc7';

//     // Fetching the data from the API
//     axios.get(apiUrl)
//     .then(response => {
//         console.log('here answer', response.data)
//         // Handle the success and display the data
//         postResults(response.data)
        
//     })
//     .catch(error => {
//         // Handle any errors
//         console.error('Error fetching data:', error);
//     });
// }



// function processInput(inputList) {
//     let recordByCustomerAndDate = {};

//     inputList.forEach(call => {
//         const { customerId, callId, startTimestamp, endTimestamp } = call;

//         // Converting time stamps
//         let startDate = new Date(startTimestamp);
//         let startDateStr = new Date(startTimestamp).toISOString().split('T')[0];
//         // we need to subtract - 1
//         let endDate = new Date(endTimestamp);
//         let endDateStr = new Date(endTimestamp).toISOString().split('T')[0];


//         let date = startDateStr;
    
//         while (date <= endDateStr) {
//             const dateObj = new Date(date);
//             console.log('==> callId', callId, 'endTimestamp', endTimestamp, 'dateObj', dateObj.getTime())

//             if(endTimestamp === dateObj.getTime()) {
//                 // we do not log when the call finishes at the same time
//                 // the day starts
//                 return;
//             }

//             if (!recordByCustomerAndDate[customerId]) {
//                 recordByCustomerAndDate[customerId] = {};
//             }
//             if (!recordByCustomerAndDate[customerId][date]) {
//                 recordByCustomerAndDate[customerId][date] = [];
//             }
            
//             recordByCustomerAndDate[customerId][date].push({
//                 callId,
//                 startTimestamp,
//                 endTimestamp
//             });

//             // Add one day (86400000) if the duration of the call is bigger than one day
//             date = new Date(new Date(date).getTime() + 86400000).toISOString().split('T')[0];
//         }
//     });

//     let results = []
//     for (let customerId in recordByCustomerAndDate) {
//         for (let date in recordByCustomerAndDate[customerId]) {
//             let result = calculateMaxConcurrency(customerId, date, recordByCustomerAndDate[customerId][date]);
//             if (result) results.push(result);
//         }
//     }

//     postResults({ results });
// }

// function calculateMaxConcurrency(customerId, date, calls) {
//     console.log('calculateMaxConcurrency', customerId, date, calls);
//     let events = []
//     calls.forEach(call => {
//         events.push({ timestamp: call.startTimestamp, type: 'start', callId: call.callId });
//         events.push({ timestamp: call.endTimestamp, type: 'end', callId: call.callId });
//     });

//     // Sorting by timestamp, when it is the same timestamp the sorting is by type === start
//     events.sort((a, b) => a.timestamp - b.timestamp || (a.type === 'start' ? -1: 1));

//     let concurrentCalls = 0;
//     let maxConcurrentCalls = 0;
//     let timestampOfMax = 0;
//     let currentCalls = new Set();
//     let callsAtMax = [];

//     events.forEach(event => {
//         if (event.type === 'start') {
//             concurrentCalls++;
//             currentCalls.add(event.callId);

//             if (concurrentCalls > maxConcurrentCalls) {
//                 maxConcurrentCalls = concurrentCalls;
//                 timestampOfMax = event.timestamp;
//                 callsAtMax = Array.from(currentCalls)
//             }
//         } else if (event.tipe === 'end') {
//             currentCalls.delete(event.callId);
//             concurrentCalls--;
//         }
//     });

//     if (maxConcurrentCalls === 0) return null;

//     return {
//         customerId: parseInt(customerId),
//         date: date,
//         maxConcurrentCalls: maxConcurrentCalls,
//         callIds: callsAtMax,
//         timestamp: timestampOfMax,
//     }
// }

// function postResults(data) {
//     const postUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=aba9ec363ad12a1bf31cd0afccc7';
//     const postTestUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/test-result?userKey=aba9ec363ad12a1bf31cd0afccc7';
//     const api = IS_TEST_MODE ? postTestUrl : postUrl;

//     console.log('TNC', data);
//     axios.post(api, data)
//         .then(response => {
//             console.log('Results posted successfully:', response.data);
//         })
//         .catch(error => {
//             console.error('Error posting results:', error);
//         });
// }

// const IS_TEST_MODE = false;

// readApi()
// //readAnswerApi()


const axios = require('axios');

const IS_TEST_MODE = false;

function readApi() {
    const apiTestUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey=aba9ec363ad12a1bf31cd0afccc7';
    const apiUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=aba9ec363ad12a1bf31cd0afccc7';
    const api = IS_TEST_MODE ? apiTestUrl : apiUrl;

    axios.get(api)
    .then(response => {
        if (!response.data || !Array.isArray(response.data.callRecords)) {
            console.error('Invalid data format:', response.data);
            return;
        }
        processInput(response.data.callRecords);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}

function processInput(inputList) {
    let recordByCustomerAndDate = {};

    inputList.forEach(call => {
        const { customerId, callId, startTimestamp, endTimestamp } = call;

        let startDate = new Date(startTimestamp);
        let endDate = new Date(endTimestamp);

        let startDateStr = startDate.toISOString().split('T')[0];
        let endDateStr = endDate.toISOString().split('T')[0];

        let date = startDateStr;
    
        while (date <= endDateStr) {
            const dateObj = new Date(date);
            if (endDate.getTime() === new Date(date).getTime()) {
                break; // No need to log this day if it ends exactly at the next day
            }
            if (endDate.getTime() === dateObj.getTime()) {
                return; // Skip logging when call finishes at the same time
            }

            if (!recordByCustomerAndDate[customerId]) {
                recordByCustomerAndDate[customerId] = {};
            }
            if (!recordByCustomerAndDate[customerId][date]) {
                recordByCustomerAndDate[customerId][date] = [];
            }
            
            recordByCustomerAndDate[customerId][date].push({
                callId,
                startTimestamp,
                endTimestamp
            });

            date = new Date(dateObj.getTime() + 86400000).toISOString().split('T')[0];
        }
    });

    let results = [];
    for (let customerId in recordByCustomerAndDate) {
        for (let date in recordByCustomerAndDate[customerId]) {
            let result = calculateMaxConcurrency(customerId, date, recordByCustomerAndDate[customerId][date]);
            if (result) results.push(result);
        }
    }

    postResults({ results });
}

function calculateMaxConcurrency(customerId, date, calls) {
    let events = [];
    calls.forEach(call => {
        events.push({ timestamp: call.startTimestamp, type: 'start', callId: call.callId });
        events.push({ timestamp: call.endTimestamp, type: 'end', callId: call.callId });
    });

    // Sort events by timestamp, 'start' before 'end'
    events.sort((a, b) => a.timestamp - b.timestamp || (a.type === 'start' ? -1 : 1));

    let concurrentCalls = 0;
    let maxConcurrentCalls = 0;
    let timestampOfMax = 0;
    let currentCalls = new Set();
    let callsAtMax = [];

    events.forEach(event => {
        if (event.type === 'start') {
            concurrentCalls++;
            currentCalls.add(event.callId);

            if (concurrentCalls > maxConcurrentCalls) {
                maxConcurrentCalls = concurrentCalls;
                timestampOfMax = event.timestamp;
                callsAtMax = Array.from(currentCalls);
            }
        } else if (event.type === 'end') {
            currentCalls.delete(event.callId);
            concurrentCalls--;
        }
    });

    if (maxConcurrentCalls === 0) return null;

    //console.log(`Processing customer ${customerId} for date ${date}`);
    //console.log('Events:', JSON.stringify(events, null, 2));
    return {
        customerId: parseInt(customerId),
        date: date,
        maxConcurrentCalls: maxConcurrentCalls,
        callIds: callsAtMax,
        timestamp: timestampOfMax,
    };
}

function postResults(data) {
    const postUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=aba9ec363ad12a1bf31cd0afccc7';
    const postTestUrl = 'https://candidate.hubteam.com/candidateTest/v3/problem/test-result?userKey=aba9ec363ad12a1bf31cd0afccc7';
    const api = IS_TEST_MODE ? postTestUrl : postUrl;

    // Ensure the output format matches the expected structure
    // console.log('Payload to be sent:', JSON.stringify(data, null, 2));
    
    axios.post(api, data)
        .then(response => {
            console.log('Results posted successfully:', response.data);
        })
        .catch(error => {
            console.error('Error posting results:', error);
        });
}

readApi();

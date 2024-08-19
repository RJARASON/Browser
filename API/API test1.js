// const apiurl = "https://api.restful-api.dev/objects"

// async function get_data() {
//     const response = await fetch(apiurl, {
//         method: "GET",
//         body: JSON.stringify({
//             "name": "Apple MacBook Pro 16",
//             "data": {
//                 "year": 2019,
//                 "price": 2049.99,
//                 "CPU model": "Intel Core i9",
//                 "Hard disk size": "1 TB",
//                 "color": "silver"
//             }
//         }),
//         headers: { "Content-Type": "application/json" }
//     });
//     console.log(await response.json());
// }
// get_data()


const apiurl = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
async function get_data() {
    const response = await fetch(apiurl, {
        method: "GET"
    });
    console.log(response);
}
get_data()



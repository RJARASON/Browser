// https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/

const apiurl = "https://api.artic.edu/api/v1/artworks/search?q=cats"

async function get_data() {
    const response = await fetch(apiurl, {
      method: 'GET'

    });
    console.log("Response is ,", response)

  };



get_data();  

// HTTP POST
// HTTP GET
// HTTP PUT
// HTTP DELECT
// HTTP PATCH






// 403
// const apiurl="https://http.cat/401"
// async function get_data(){
//     const response=await fetch(apiurl,{
//         method:"PATCH"
//     });
//     console.log(response);
// }
// get_data()


// 405
// const api="https://picsum.photos/200/300"
// async function get_data(){
//     const response=await fetch(api,{
//         method:"PUT"
//     });
//     console.log(response);
// }
// get_data()


// 405
// const apiurl="https://collectionapi.metmuseum.org/public/collection/v1/objects/100"
// async function get_data(){
//     const response=await fetch(apiurl,{
//         method:"DELECT"
//     });
//     console.log(response);
// }
// get_data()



//200
// const apiurl="https://php-noise.com/noise.php?hex=FFFFFF&json"
// async function get_data(){
//     const response=await fetch(apiurl,{
//         method:"PATCH"
//     });
//     console.log(response);
// }
// get_data()



// 200
// const apiurl="https://placebear.com/200/300"
// async function get_data(){
//     const response=await fetch(apiurl,{
//         method:"GET"
//     });
//     console.log(response);
// }
// get_data()


// 404
// const apiurl="https://random.dog/woof.json"
// async function get_data(){
//     const response=await fetch(apiurl,{
//         method:"POST"
//     });
//     console.log(response);
// }
// get_data()










  
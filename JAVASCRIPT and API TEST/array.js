// function Words() {
//   let words = "photosyntesis";
//   for (let i = 0; i < words.length; i++) {
//     console.log(words.substring(0, words.length - i));
//   }
// }

// const { By, until } = require("selenium-webdriver");
// const commontask = require("../helpers/commontask");
// const USSDTest = require("../PageObjects/ussdobjects");
// const checkpoint = require("../helpers/checkpoint");
// const { page } = require("pdfkit");
// const ussdobjects = require("../PageObjects/ussdobjects");
// const { Extensions } = require("selenium-webdriver/chromium");

//Function to count from 1 - 100

//Function to put each letter in  your full name into an array

//Function to print that will print tintinnabulation while subtracting
//the last letter on multiple events untill there's no letter left

//Create a function that logs the name and second course for every person in the data

//Locations, entities' types, educational levels that are true, second course

// let arr = ["k", "o", "d", "j", "o"];
// let data = [
//   {
//     name: "John",
//     courses: ["Mathematics 101", "Physics 201", "Biology 101"],
//   },
//   {
//     name: "Emily",
//     courses: ["History 101", "Literature 201", "Chemistry 101"],
//   },
//   {
//     name: "David",
//     courses: ["Economics 101", "Computer Science 201", "Psychology 101"],
//   },
//   {
//     name: "Sarah",
//     courses: ["English Composition", "Art Appreciation", "Sociology 101"],
//   },
//   {
//     name: "Michael",
//     courses: ["Philosophy 101", "Language Studies", "Anthropology 101"],
//   },
//   {
//     name: "Jessica",
//     courses: [
//       "Business Management",
//       "Communication Skills",
//       "Environmental Studies",
//     ],
//   },
//   {
//     name: "Andrew",
//     courses: ["Statistics 101", "Dance Theory", "Theater Arts"],
//   },
//   {
//     name: "Rachel",
//     courses: ["Geology 101", "Architecture Design", "Music Theory"],
//   },
//   {
//     name: "Kevin",
//     courses: [
//       "Political Science 101",
//       "Education Foundations",
//       "Agriculture Studies",
//     ],
//   },
//   {
//     name: "Amanda",
//     courses: ["Astronomy 101", "Engineering Fundamentals", "Health Sciences"],
//   },
//   {
//     name: "Daniel",
//     courses: ["Law and Society", "Criminology 101", "Ethics in Practice"],
//   },
//   {
//     name: "Michelle",
//     courses: ["Linguistics 101", "Advanced Mathematics", "Microeconomics"],
//   },
//   {
//     name: "Jason",
//     courses: [
//       "Composition and Rhetoric",
//       "Cultural Anthropology",
//       "Marketing Strategies",
//     ],
//   },
//   {
//     name: "Hannah",
//     courses: [
//       "Archaeology 101",
//       "Science Fiction Literature",
//       "Abnormal Psychology",
//     ],
//   },
//   {
//     name: "Benjamin",
//     courses: ["Physical Education", "Modern Dance", "Environmental Science"],
//   },
//   {
//     name: "Stephanie",
//     courses: ["Art History", "Genetics", "Social Work"],
//   },
//   {
//     name: "Eric",
//     courses: [
//       "Philosophy of Mind",
//       "International Relations",
//       "Curriculum Development",
//     ],
//   },
//   {
//     name: "Olivia",
//     courses: ["World History", "Creative Writing", "Public Speaking"],
//   },
//   {
//     name: "Peter",
//     courses: ["Macroeconomics", "Software Engineering", "Child Development"],
//   },
//   {
//     name: "Amy",
//     courses: ["Exercise Physiology", "Statistics", "Forensic Anthropology"],
//   },
// ];

// function Getdata() {
//     data.forEach(stud => {
//         const name = stud.name;
//         const course = stud.courses[1]
//         console.log(`NAME ${name}  COURSES ${course}`);
//     })
// }

// const formatData = (locations) => {
//   const result = {};
//   locations.forEach((location) => {
//     const cityName = location.name;
//     location.entities.forEach((entity) => {
//       if (entity.type === "school") {
//         if (!result[cityName]) {
//           result[cityName] = { Entities: [] };
//         }

//         const secondCourse = entity.courses[1];
//         const educationLevels = Object.keys(entity.education_levels).filter(
//           (level) => entity.education_levels[level]
//         );

//         result[cityName].Entities.push({
//           entityType: entity.type,
//           course: secondCourse,
//           education_levels: educationLevels,
//         });
//       }
//     });
//   });

//   return result;
// };

// const formattedData = formatData(locations);
// console.log(JSON.stringify(formattedData, null, 2));

let locations = [
  {
    name: "New York",
    entities: [
      {
        type: "school",
        name: "Central High School",
        courses: ["Mathematics", "Science", "Literature"],
        education_levels: {
          preschool: true,
          creche: false,
          college: true,
        },
      },
      {
        type: "school",
        name: "Downtown Elementary",
        courses: ["Art", "History", "Physical Education"],
        education_levels: {
          preschool: true,
          creche: false,
          college: false,
        },
      },
      {
        type: "hospital",
        name: "City Hospital",
        services: ["Emergency Care", "Surgery", "Pediatrics"],
      },
    ],
  },
  {
    name: "Los Angeles",
    entities: [
      {
        type: "school",
        name: "Westside High School",
        courses: ["Computer Science", "Music", "Foreign Languages"],
        education_levels: {
          preschool: false,
          creche: false,
          college: true,
        },
      },
      {
        type: "hospital",
        name: "Sunset Medical Center",
        services: ["Internal Medicine", "Cardiology", "Oncology"],
      },
    ],
  },
];

let school = [];
let Entities = [];
locations.forEach((location) => {
  location.entities.forEach((entity) => {
    if (entity.type === "school" && entity.education_levels.college) {
      Entities.push({
        location: location.name,
        entityType: entity.type,
        educationLevels: entity.education_levels,
        secondCourse: entity.courses[1],

      });
    if(entity.type==="hospital"&&entity.type&&entity.name&&entity.services){
      Entities.push({
        location:location.name,
        entityType: entity.type,
        entityType: entity.services
      });
    }
    }
    if (entity.type === "school") {
      school.push(entity.name);
    }
  });
});
console.log(Entities);
console.log(school);
//for (let stud = 0; data.length; )
// data
// let banks = [
//   { name: "Bank of America", location: "New York" },
//   { name: "Chase Bank", location: "California" },
//   { name: "Wells Fargo", location: "Texas" },
//   { name: "Citibank", location: "Illinois" },
//   { name: "HSBC", location: "Florida" },
//   { name: "TD Bank", location: "New Jersey" },
//   { name: "PNC Bank", location: "Pennsylvania" },
//   { name: "US Bank", location: "Minnesota" },
//   { name: "Capital One", location: "Virginia" },
//   { name: "BB&T", location: "North Carolina" },
// ];

// function for_loop() {
//   for (let counter = 0; counter < banks.length; counter++) {
//     const Bank = banks[counter];
//     const bankname = Bank.name;
//     const locate = Bank.location;
//     console.log(bankname);
//     console.log(locate);
//   }
// }

// function add_one() {
//   let counter = 1;
//   counter += 1;
//   console.log("counter is ", counter);
// }

// function getnum100() {
//   let num = 1;
//   while (num < 100) {
//     // num=+1
//     console.log((num += 1));
//   }
// }

// function getletter() {
//   let name = "Kodjo";
//   na = name.split("");
//   console.log(na);
// }

// function getnumback() {
//   let word = "tintinnabulationiphjk";
//   for (let i = 0; i < word.length; i++) {
//     console.log(word.substring(3, word.length - i));
//   }
// }

// describe("GET NUM", async function () {
//   before(async function () {
//     /*  this.Sample = await commontask.get_data('kwmZfIGsFqdMluIS')
//          this.number = await commontask.get_data("XRQLJXEwZ4NRZbc2")
//          this.affiliate = await commontask.get_data("nkXOuBYrsArHZz3w")
//          this.language = await commontask.get_data("WASOUkx3VrZWZp9Z")
//          this.base_url_endpoint = await commontask.get_data("lVqzQBvErXCUziiE") */
//     //await USSDTest.startApp(this.number, this.affiliate, this.language, this.base_url_endpoint)
//     //await new Promise((resolve) => setTimeout(resolve, 5000))
//   });

//   it.only("Go to check balance", async function () {
//     // getnum100()
//     // getletter()
//     // getnumback()
//     // while_loop()
//     location();
//     //print_name("Paul Steiner")
//     /* await USSDTest.submitInputText("*326#")
//         await USSDTest.waitForDialog()
//         await USSDTest.submitInputText("7")
//         await USSDTest.waitForDialog()
//         await USSDTest.submitInputText("1")
//         await USSDTest.waitForDialog()
//         let pageResponse = await USSDTest.getResponseText()
//         console.log("page response; ", pageResponse) */
//     /* let rep = "page response;  Select Account:
//         1. 001xxx322 - NGN
//         2. 0011207585
//         3. 012xxx608 - NGN
//         4. 050xxx367 - NGN
//         5. 113xxx124 - NGN
//         6. 394xxx281 - NGN
//         7. 533300" */

//     /*  let acc_num = [1, 1, 0,9,1,3,2,2]
//          console.log(acc_num.slice(2)); */
//   });

//   it("Slash 'N' it", async function () {
//     let acc_num = "001109322";
//     let lastThreeNum = acc_num.slice(-3);
//     let rep =
//       "page response;  Select Account:\n1. 001xxx322 - NGN\n2. 0011207585\n3. 012xxx608 - NGN\n4. 050xxx367 - NGN\n5. 113xxx124 - NGN\n6. 394xxx281 - NGN\n7. 5333002146";
//     let arr = rep.split("\n");
//     for (let i = 0; i < arr.length; i++) {
//       if (arr[i].includes(lastThreeNum)) {
//         console.log("yayyy. Found it at ", i);
//         break;
//       }
//     }
//     arr.forEach((boxes, index) => {
//       boxes.includes(lastThreeNum)
//         ? console.log("yayyy. Found it at ", index)
//         : "";
//     });
//     //console.log("arr is; ", arr)
//   });

//   i;

//   after(async function () {});
// });

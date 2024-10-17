const data = [
  { name: "John", courses: ["Mathematics 101", "Physics 201", "Biology 101"] },
  {
    name: "Emily",
    courses: ["History 101", "Literature 201", "Chemistry 101"],
  },
  {
    name: "David",
    courses: ["Economics 101", "Computer Science 201", "Psychology 101"],
  },
  {
    name: "Sarah",
    courses: ["English Composition", "Art Appreciation", "Sociology 101"],
  },
  {
    name: "Michael",
    courses: ["Philosophy 101", "Language Studies", "Anthropology 101"],
  },
  {
    name: "Jessica",
    courses: [
      "Business Management",
      "Communication Skills",
      "Environmental Studies",
    ],
  },
  {
    name: "Andrew",
    courses: ["Statistics 101", "Dance Theory", "Theater Arts"],
  },
  {
    name: "Rachel",
    courses: ["Geology 101", "Architecture Design", "Music Theory"],
  },
  {
    name: "Kevin",
    courses: [
      "Political Science 101",
      "Education Foundations",
      "Agriculture Studies",
    ],
  },
  {
    name: "Amanda",
    courses: ["Astronomy 101", "Engineering Fundamentals", "Health Sciences"],
  },
  {
    name: "Daniel",
    courses: ["Law and Society", "Criminology 101", "Ethics in Practice"],
  },
  {
    name: "Michelle",
    courses: ["Linguistics 101", "Advanced Mathematics", "Microeconomics"],
  },
  {
    name: "Jason",
    courses: [
      "Composition and Rhetoric",
      "Cultural Anthropology",
      "Marketing Strategies",
    ],
  },
  {
    name: "Hannah",
    courses: [
      "Archaeology 101",
      "Science Fiction Literature",
      "Abnormal Psychology",
    ],
  },
  {
    name: "Benjamin",
    courses: ["Physical Education", "Modern Dance", "Environmental Science"],
  },
  { name: "Stephanie", courses: ["Art History", "Genetics", "Social Work"] },
  {
    name: "Eric",
    courses: [
      "Philosophy of Mind",
      "International Relations",
      "Curriculum Development",
    ],
  },
  {
    name: "Olivia",
    courses: ["World History", "Creative Writing", "Public Speaking"],
  },
  {
    name: "Peter",
    courses: ["Macroeconomics", "Software Engineering", "Child Development"],
  },
  {
    name: "Amy",
    courses: ["Exercise Physiology", "Statistics", "Forensic Anthropology"],
  },
];

data.forEach((student) => {
  const name = student.name;
  const secondCourse = student.courses[1];
  console.log(`Name: ${name}, Second Course: ${secondCourse}`);
});

export default function getListStudents () {
  const studentList = [];

  const student1 = {
    id: 1,
    firstName: "Guillaume",
    location: "San Francisco"
  }

  studentList.push(student1);

  const student2 = {
    id: 2,
    firstName: "James",
    location: "Columbia"
  };
  studentList.push(student2);

  const student3 = {
    id: 5,
    firstName: "Serena",
    location: "San Francisco"
  };
  studentList.push(student3);

  return studentList;
}

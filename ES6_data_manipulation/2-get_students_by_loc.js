export default function getStudentsByLocation(studentList, city) {
  const studentCity = studentList.filter((student) => student.location === city);
  return studentCity;
}

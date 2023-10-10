export default function getStudentIdsSum(studentList) {
  const idsSum = studentList.reduce((accumulator, student) => accumulator + student.id, 0);
  return idsSum;
}

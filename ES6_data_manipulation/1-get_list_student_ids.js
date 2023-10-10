export default function getListStudentIds(studentList) {
  if (Array.isArray(studentList)) {
    const ids = studentList.map((student) => student.id);
    return ids;
  }
  return [];
}

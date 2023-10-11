export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const studentsInCity = studentList.filter((student) => student.location === city);

  const studentsWithGrades = studentsInCity.map((student) => {
    const studentGrade = newGrades.find((grade) => grade.studentId === student.id);
    if (studentGrade) {
      return {
        ...student,
        grade: studentGrade.grade,
      };
    }
    return {
      ...student,
      grade: 'N/A',
    };
  });

  return studentsWithGrades;
}

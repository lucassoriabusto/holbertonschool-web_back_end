import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  Promise.all(promises)
    .then((results) => {
      const [photoResult, userResult] = results;

      console.log('body', userResult.body);
      console.log('firstName', userResult.firstName);
      console.log('lastName', userResult.lastName);
    })
    .catch((error) => {
      console.error('Signup system offline');
    });
}

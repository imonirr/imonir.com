const Octokit = require('@octokit/rest')
const {
  githubAccessToken,
} = require('config/vars');

const gitClient = new Octokit({
  auth: githubAccessToken,
});
// GITHUB_ACCESS_TOKEN

// exports.getList = async () => {
//   try {
//     debugApp('Remove User: ' + id);
//     await User.findOneAndRemove({ _id: id });
//     return true;
//   } catch (err) {
//     throw err;
//   }
// }

exports.test = async () => {
  console.log('github token: ' + githubAccessToken);

  try {

    const readme = await gitClient.repos.getReadme({
      owner: 'dostokhan',
      repo: 'dostokhan.github.io',
      path: 'README.md',
      mediaType: {
        format: 'application/vnd.github.VERSION.html',
      }
    });
    const content = readme.data.content;
    let buff = new Buffer(content, 'base64');
    let text = buff.toString('ascii');
    console.log(text);
    console.log('html CONTENT above');

    buff = new Buffer(content, 'base64');
    text = buff.toString('ascii');
    console.log(text);
  // try {
  //   debugApp('Remove User: ' + id);
  //   // await User.findOneAndRemove({ _id: id });
  //   return true;
  // } catch (err) {
  //   throw err;
  // }
    // await User.findOneAndRemove({ _id: id });
    return true;
  } catch (err) {
    throw err;
  }
};

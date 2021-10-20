const fs = require('fs');

const chirpViews = JSON.parse(fs.readFileSync("D:/Fall 2021/Mfgx/chirpViews.json"));
/*
  Method to return a formatted string based on the input Object
  Accepts a JSON Object containing message, date, views, author as the properties
  Returns formatted string.
*/

/*
  Setting the default parameter value of chirpView as an empty Object
  so that destructuring doesn't fail if chirpView is undefined
*/
const formatChirpView = (chirpView = {}) => {
  const {
    message,
    date,
    views,
    author
  } = chirpView;
  /*
    Assuming that the requirement is to return
    if one of the values is not present
  */
  if (!message || !date || !views || !author) {
    return '';
  }
  let formattedMessage = '';
  const trendingChirpLimit = 100000;
  const chirpCharacterLimit = 140;

  const dateObject = new Date(date);
  // Scope for improvement => Check if dateObject is a valid date

  const formattedDate = dateObject.toLocaleDateString(
    'en-US', {

    month: '2-digit',
    day: '2-digit',
    year: 'numeric',
    timeZone: 'UTC'
  }
  );

  let chirpInfo = `${formattedDate} ${views} ${author}`;
  //Adding Fire Emoji If Views greater than 100000
  if (views > trendingChirpLimit) {
    chirpInfo += " 🔥";
  }

  formattedMessage = `${message} ${chirpInfo}`;
  //Slicing if Length of Characters is greater than 140
  if (formattedMessage.length > chirpCharacterLimit) {
    formattedMessage = `${message.slice(0,(chirpCharacterLimit - 1 - chirpInfo.length - 3))} ... ${chirpInfo}`;
  }

  return formattedMessage;
};
chirpViews.map((chirpView) => console.log(formatChirpView(chirpView)));

module.exports = {
  formatChirpView,
};

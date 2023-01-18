//Exercise1
var sentence = "The movie is not that bad, I like it";
wordNot = sentence.indexOf("not");
wordBad = sentence.indexOf("bad");


if (wordBad > wordNot) {
    let goodSentence = sentence.substring(wordNot, wordBad + 3);
    console.log(sentence.replace(goodSentence, "good"));
} else {console.log(sentence);
}
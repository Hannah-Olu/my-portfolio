import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';
const myWork = [
  {
    'title': "Work Example",
    'href': "https://example.com",
    'desc': "Amet excepteur consectetur adipisicing do voluptate cupidatat Lorem fugiat nulla.",
    'image': {
      'desc': "example screenshot of a project involving code",
      'src': "images/example1.png",
      'comment': ""
    }
  },
  {
    'title': "About Me",
    'href': "https://example.com",
    'desc': "Mollit labore qui ullamco deserunt voluptate velit ea ipsum incididunt.",
    'image': {
      'desc': "A Severless Portfolio",
      'src': "images/example2.png",
      'comment': ""
    }
  },
  {
    'title': "Work Example",
    'href': "https://example.com",
    'desc': "Quis enim qui anim amet ipsum nulla in duis aliquip anim.",
    'image': {
      'desc': "example screenshot of a project involving cats",
      'src': "images/example3.png",
      'comment': `Cloud is about how you do computing, and not where you do computing

      -Paul Marity`
    }
  },
  {
    'title': "Portrait",
    'href': "https://example.com",
    'desc': "Quis enim qui anim amet ipsum nulla in duis aliquip anim.",
    'image': {
      'desc': "example screenshot of a project involving cats",
      'src': "images/portrait.jpg",
      'comment': `Cloud is about how you do computing, and not where you do computing

      -Paul Marity`
    }
  },
]
ReactDOM.render(<ExampleWork work={myWork} />, document.getElementById('example-work'));
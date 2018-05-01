import React, { Component } from 'react';
import './Login.css';
import {loadingCss} from "./Login";
import axios from "axios/index";

class WordCounter extends Component {
    constructor(){
        super();
        this.state = {
            loading: false,
            resultFound: false,
            words : [],
            currentWord: null,
            url: null,
            message: null
        }
    }
    countWords(){
        this.setState({loading: true});
        let self = this;
      axios.post('/count', {
          words: this.state.words,
          url: this.state.url
        }, {
          headers: { 'Content-Type': 'text/plain' }})
        .then(function (response) {
          self.setState({resultFound: true, loading: false})
        })
        .catch(function (error) {
          self.setState({message: error, loading: false});
          console.log(error);
        });
    }

    addWord(){
        let stateWords = this.state.words;
        if(!stateWords.includes(this.state.currentWord)
            && this.state.currentWord !== null) {
            stateWords.push(this.state.currentWord);
            this.setState({words: stateWords})
        }
    }
      handleChange = name => event => {
    this.setState({
      [name]: event.target.value,
    });
  };
  render() {
      let words = this.state.words;
      words = this.mapWords(words);
    const formWordsCount = (
        <div className="login-form form-group">
            <div className="form-group">
                <h3>Target URL</h3>
                <input className="form-input"
                onChange={this.handleChange('url')}/>
            </div>
            <div className="form-group">
                <h3>words match</h3>
                {words}
                <input className="form-input"
                       onChange={this.handleChange('currentWord')}  />
               <button onClick={this.addWord.bind(this)}
              className="login-button">Add</button>
            </div>
            <div className="form-group">
                <button onClick={this.countWords.bind(this)}
              className="login-button">Count</button>
            </div>
        </div>
    );
    let display = this.state.loading? loadingCss: formWordsCount;
    display = this.state.resultFound? this.getResult(): display;
    return (
        <div>
            {display}
        </div>
    )
  }

    mapWords(words) {
        const wordsRender = words.map((word) =>
          <li key={word}><h3>{word}</h3></li>
        );
        return (<ul>
            {wordsRender}
        </ul>)
    }

    getResult() {

    }
}

export default WordCounter;

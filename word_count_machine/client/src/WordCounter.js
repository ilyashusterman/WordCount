import React, { Component } from 'react';
import axios from "axios/index";
import Typography from 'material-ui/Typography';
import Popover from 'material-ui/Popover';
import {loadingCss} from "./Login";
import './Login.css';

class WordCounter extends Component {
    constructor(){
        super();
        this.state = {
            loading: false,
            resultFound: false,
            resultCount: null,
            words : [],
            currentWord: null,
            url: null,
            message: null
        }
    }

    countWords(event){
        this.setState({loading: true});
        let self = this;
        let requestWords = this.state.words;
        let requestUrl = this.state.url;
        if (requestWords.length>0 && requestUrl!== null) {
            axios.post('/count', {
                words: requestWords,
                url: requestUrl
            }, {
                headers: {'Content-Type': 'text/plain'}
            })
                .then(function (response) {
                    self.setState({
                        resultFound: true, loading: false,
                        resultCount: response.data,
                        message: null
                    })
                })
                .catch(function (error) {
                    self.setState({message: error.message, loading: false,
                    anchorEl: event.currentTarget
                    });
                });
        }else{
            this.setState({loading: false,
                anchorEl: event.currentTarget,
                message: 'Please add words'})
        }
    }
    resetWords(){
        this.setState({
            loading: false,
            resultFound: false,
            resultCount: null,
            words : [],
            currentWord: null,
            url: null,
            message: null,
            anchorEl: null,
        })
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
     handleClose = () => {
    this.setState({
      anchorEl: null,
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
                <h3>words for match</h3>
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
    let display = this.state.loading? this.getLoading(): formWordsCount;
    display = this.state.resultFound? this.getResult(): display;
    let message = this.state.message !== null? this.displayMessage(): null;
    console.log('state.message', this.state.message);
    console.log('message', message);
    return (
        <div>
            {display}
            {message}
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
        let results = this.state.resultCount;
        let resultsList = [];
        Object.keys(results).forEach(function(key) {
            resultsList.push({'word': key, 'count': results[key]});
        });
        let listItems = resultsList.map((word) =>
            <li key={word['word'].toString()}>
                <h3>  {word['word']}: {word['count']}</h3>
            </li>
          );
        if (listItems.length<1){
            listItems = (<h1>Nothing found :(</h1>)
        }
          return (
              <div>
                  <h1>Done! this is what is counted</h1>
            <ul>{listItems}</ul>
                  <button onClick={this.resetWords.bind(this)}
                          className="login-button" >Start over</button>
              </div>
          );
    }

    getLoading() {
        return (
            <div>
                <h1>Counting Words...</h1>
                {loadingCss}
           </div>
        );
    }

    displayMessage() {
      const { anchorEl } = this.state;
      const { message } = this.state;
      return (<Popover
          open={Boolean(anchorEl)}
          anchorEl={anchorEl}
          onClose={this.handleClose}
          anchorOrigin={{
            vertical: 'bottom',
            horizontal: 'center',
          }}
          transformOrigin={{
            vertical: 'top',
            horizontal: 'center',
          }}
        >
          <Typography>{message}</Typography>
        </Popover>)
    }
}

export default WordCounter;

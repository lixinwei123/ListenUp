import { Http,RequestOptions,BaseRequestOptions,Headers } from '@angular/http';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams,LoadingController} from 'ionic-angular';
import {User } from "../../models/user";
import {AngularFireAuth} from 'angularfire2/auth';
import { Platform } from 'ionic-angular';
import { MenuController } from 'ionic-angular';
import { TabsPage } from '../tabs/tabs';
import {UserInfoProvider} from '../../providers/userInfo/userInfo';
import {CreateuserPage} from '../createuser/createuser';
//import * as firebase from 'firebase';
import {RegisterPage} from '../register/register';
import { LinkedIn } from '@ionic-native/linkedin';
import * as firebase from 'firebase/app';
import { InAppBrowser } from '@ionic-native/in-app-browser';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { HTTP } from '@ionic-native/http';
import 'rxjs/add/operator/map';
import {AlertController} from 'ionic-angular';
import { Observable } from 'rxjs/Observable';
// import {Injectable} from '@angular/core';
// import 'rxjs/add/operator/map';
/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
// @Injectable()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',

})
export class LoginPage {
  usrInfo: any;
  allUsers: any;
  log = false;
  reg = false;
  rootPage: any = LoginPage;
  user = {} as User;
  scopes: any[] = ['r_basicprofile', 'r_emailaddress'];
  accessToken: any;
  isLoggedIn: any;
  window: any;
  firstHead: any;
  testingInfo: any;
  testingBool = false;
  linkedinUri = "https://www.linkedin.com/oauth/v2/authorization?format=json&response_type=code&client_id=7818gxiruyce0r&redirect_uri=http://localhost:8100/callback&state=Listenuptesting&r_basicprofile%20r_emailaddress"
  apiUrl = 'https://us-central1-listenuptesting.cloudfunctions.net/createFirebaseToken';
  // serviceAccount = require();
  selfData = { id:"", firstName:"", lastName:"" };
  constructor(private afAuth: AngularFireAuth,
    public navCtrl: NavController, 
    public navParams: NavParams, 
    public platform : Platform, 
    public uInfo: UserInfoProvider,
    public menuCtrl: MenuController,
     private linkedin: LinkedIn,
     private http: Http,
    public inApp: InAppBrowser,
    public load: LoadingController,
    public httpPlug: HTTP,
    public alertCtrl: AlertController,
    public httpClient: HttpClient) { 
      this.menuCtrl.swipeEnable(false);
  }

  async login(user: User) {
    this.log = true;
    try {
      const result = await this.afAuth.auth.signInWithEmailAndPassword(user.email, user.password);
      if (result) {
        console.log('result',result);
        this.loadUserInfo();
       this.navCtrl.setRoot(TabsPage);
      }
    }
  catch(e){
    console.error(e);
    }
  }

// linkedInlLogin(){
//    this.linkedin.login(this.scopes, true)
//     .then(() => console.log('Logged in!'))
//     .catch(e => console.log('Error logging in', e));
   

// }

askCloud(id){
      let url = `https://us-central1-listenuptesting.cloudfunctions.net/createFirebaseToken`
    let params: URLSearchParams = new URLSearchParams();
    // let headers = new Headers({'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });

    params.set('linkedin',id);
    return this.http.post(url, params)
                    .toPromise()
                    .then( res => {
                      console.log(res)
                    })
                    .catch(err => {
                      console.log(err)
                    })

  }

 
linkedLogin() {
    this.linkedin.login(this.scopes, true)
        .then((success) => {
          console.log("success time",success);
            this.isLoggedIn = true;
            this.getSelfData();
            this.linkedin.getActiveSession().then((token) => {
            this.accessToken = token;
    })
        })
        .catch(e => console.log('Error logging in', e));
}



// linkedInLogin(){

//   let browserRef = window.open(this.linkedinUri, '_blank', 'location=no');
//     browserRef.addEventListener("?code=", (event: any) => {
//       if ((event.url).indexOf('?code=') !== -1) {
//         let token = event.url.slice(event.url.indexOf('?code=') + '?code='.length);
//         // here is your token, now you can close the InAppBrowser
//         browserRef.close();
//         console.log("token is",token);
//       }
//     })
//   // this.http.get('').subscribe((data) => {
//   //   console.log("data",data.text())
//   // })
// }

getLinkCode(){
  var inApp = this.inApp
  var linkedinUri = this.linkedinUri
  var load = this.load
  var headers = new Headers();
  headers.append('Content-Type','application/x-www-form-urlencoded')
  headers.append('Host','www.linkedin.com')
  var options = new RequestOptions({
    headers: headers
  })
  var http = this.http
   return new Promise(function(resolve, reject) {
        var browserRef = window.open(linkedinUri, "_blank", "location=no,clearsessioncache=yes,clearcache=yes");
        browserRef.addEventListener("loadstart", (event: any) => {
            if ((event.url).indexOf("localhost:8100/callback") === 0) {
                browserRef.removeEventListener("exit", (event) => {});
                browserRef.close();
                console.log("EVENT",event.url);
                console.log("event.url 2 -> " + event.url);
                var parsedResponse = {};
                var code = (event.url.split("=")[1]).split("&")[0];
                var state = event.url.split("=")[2];
                if (code !== undefined && state !== null) {
                  console.log("code : " + code + "  state : " + state);
                  parsedResponse["code"] = code;
                  //parsedResponse["state"] = state;
                  resolve(parsedResponse);
                } else {
                  reject("Problem authenticating with LinkedIn");
                }
            }
        });
        browserRef.addEventListener("exit", function(event) {
            reject("The Linkedin sign in flow was canceled");
        });
    });
}
getToken(code){
    var authorizationURL = 'https://www.linkedin.com/oauth/v2/authorization';
    var client_id = '7818gxiruyce0r';
      var redirect_uri = 'http://milord-homedesk.ngrok.io.ngrok.io/callback';
      var state = 'listenuplogin';
    var urlString = 'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id='+ client_id
    +'&redirect_uri=' +redirect_uri+ '&state='+state;

      if(this.platform.is('android')){
        window.open(urlString);
      }
      else if(this.platform.is('ios')){
        window.location.href = urlString;
      }
      else{
        window.open(urlString);
      }
  
}
linkedInLogin(){
  let loader;
  this.platform.ready().then(() => this.getLinkCode().then((success: any) => {
    console.log("SUccess" + success.code);
    var data = "grant_type=authorization_code&code=" + success.code + "&redirect_uri=http://localhost:8100/callback&client_id=7818gxiruyce0r&client_secret=gGmAzVSZ1C1Qlws2"
      var dat = {
      grant_type:"authorization_code",
      code: success,
      redirect_uri:'redirect_uri=http://localhost:8100/callback',
      client_id:'7818gxiruyce0r',
      client_secret:'gGmAzVSZ1C1Qlws2'
    }

     this.httpPlug.setDataSerializer('urlencoded');
     this.httpPlug.post("https://www.linkedin.com/oauth/v2/accessToken",dat,{"Content-Type":"application/x-www-form-urlencoded"}).then(res => {
       let result = res
       if(result){
         this.testingBool = true
       }
       this.testingInfo = result
       console.log("http result:",result);
     },
     fail => {
       console.log("FAILURE",fail);
     }
     );
      }));
}

  loadUserInfo(){
    this.usrInfo = this.uInfo.getUserInfo();
    if (this.usrInfo == undefined || this.usrInfo == null){
      setTimeout(() => {

        this.loadUserInfo();
      },1000);
    }
  }

  getSelfData() {
    this.linkedin.getRequest('people/~')
        .then(res => {
            this.selfData = res;
            console.log("DATA TIME BITCHES",res);
            var token = this.askCloud(res.id)
        })
        .catch(e => console.log(e));
    }

ionViewDidAppear() {
    this.linkedin.hasActiveSession().then((active) => {
        this.isLoggedIn = active;
        if(this.isLoggedIn === true) {
            this.getSelfData();
        }
    });
}


 signInWithToken(token){
  firebase.auth().signInWithCustomToken(token).catch(function(error) {
  var errorCode = error.code;
  var errorMessage = error.message;
});
 }

createToken(id){
 // this.http.get('https://us-central1-listenuptesting.cloudfunctions.net/createFirebaseToken?id=' + id).subscribe((data) => {
 //   console.log("data",data.text());
 //   this.signInWithToken(data.text());
 // })
 this.signInWithToken('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJyNTE1eSIsImlhdCI6MTUzMTYzNzM4OSwiZXhwIjoxNTMxNjQwOTg5LCJhdWQiOiJodHRwczovL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsImlzcyI6ImZpcmViYXNlLWFkbWluc2RrLW5oY2phQGxpc3RlbnVwdGVzdGluZy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsInN1YiI6ImZpcmViYXNlLWFkbWluc2RrLW5oY2phQGxpc3RlbnVwdGVzdGluZy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSJ9.FfZk49OiOr6NGQxuair6LZY-Hih6gJgnjAV2oAXojp30cQTbzVqdcySYmaI2bvfGQ2tlw-8n-bxMz2KXNxPKXwumS6BEZkwVjWnkWheQiu-mjQDhD307nuQoRBNI1rTeWc46C2EUZ1bm8w9MkkEkQLrMMem9W-lzvQcHBWrmdMqSztgQGHiEy-vQMuJy78bjhY0vMMTe3ro7Ai9FG0SHKUE-21DLFveMpvTsgNQtFwoD5HMDULoNkOpDO001V_tgeTmbjK2s3zUY3ZzE6ZpWUzFu_4PBw1Ipx0FRVFkwdL2NgSg1Q0lmX5bRTNy86idH4px-D2Ax4Fn4mQyBXXzeBw')
}
checkToken(){
  var token = this.createToken('R15815')
  console.log("TOKEN",token);
}
  register(){
    this.navCtrl.push(RegisterPage);
  }








}

import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule} from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule, NavController } from 'ionic-angular';
import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';
import { BarcodeScanner } from '@ionic-native/barcode-scanner';
import {AngularFireModule} from "angularfire2";
import {AngularFireAuth } from "angularfire2/auth";
import { MyApp } from './app.component';
import {FIREBASE_CONFIG} from "./app.firebase.config";
import { LinkedIn } from '@ionic-native/linkedin';
import { InAppBrowser } from '@ionic-native/in-app-browser';
import{AngularFireDatabaseModule} from 'angularfire2/database';
import { Slides } from 'ionic-angular';
import { ViewChild } from '@angular/core';
import { TabsPage } from '../pages/tabs/tabs';
import {LoginPage} from '../pages/login/login';
import {RegisterPage} from '../pages/register/register';
// import {SendfeedPage} from '../pages/sendfeed/sendfeed';
// import {SearchuserPage} from '../pages/searchuser/searchuser';
import {CreateuserPage} from '../pages/createuser/createuser';
import {BlockusersPage} from '../pages/blockusers/blockusers';
import {ComponentsModule} from '../components/components.module';
import {TermsOfServicesPage} from '../pages/terms-of-services/terms-of-services';
// import {SettingsPage} from '../pages/settings/settings';

//Import Modal
import {TermsOfServiceModal} from '../pages/register/termsofservice-modal';
import {EditProfilePage} from '../modals/edit-profile/edit-profile';

import { UserInfoProvider } from '../providers/userInfo/userInfo';
import { Camera } from '@ionic-native/camera';

 import {FeedbacktitlePage} from '../pages/feedbacktitle/feedbacktitle';
import { PipesModule } from '../pipes/pipes.module';
import { ChatInfoProvider } from '../providers/chat-info/chat-info';
import { IonicStorageModule } from '@ionic/storage';
// import { IonicImageLoader } from 'ionic-image-loader';
import { HttpModule} from '@angular/http';
import { Http,Headers } from '@angular/http';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { HTTP} from '@ionic-native/http';
@NgModule({
  declarations: [
    MyApp,
    // FeedbackPage,
    // MessagePage,
    // ProfilePage,
    RegisterPage,
    TabsPage,
    LoginPage,
    FeedbacktitlePage,
    // SendfeedPage,
    // SearchuserPage,
    CreateuserPage,
    BlockusersPage,
    // SettingsPage,
    // TermsOfServicesPage,
      TermsOfServiceModal,
      EditProfilePage,
      

  ],
  imports: [
    BrowserModule,
    HttpModule,
    HttpClientModule,
    IonicModule.forRoot(MyApp,{
        mode: 'ios',
        iconMode: 'ios',
        backButtonText: ''
    }),
    AngularFireModule.initializeApp(FIREBASE_CONFIG),
    AngularFireDatabaseModule,
    PipesModule,
    ComponentsModule,
    IonicStorageModule.forRoot(),





    // IonicImageLoader.forRoot()
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    RegisterPage,
    TabsPage,
    FeedbacktitlePage,
    // SendfeedPage,
    // SearchuserPage,
    CreateuserPage,
    BlockusersPage,
    LoginPage,
    // SettingsPage,
    // TermsOfServicesPage,
    TermsOfServiceModal,
    EditProfilePage,

  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    AngularFireAuth,
    AngularFireDatabaseModule,
    UserInfoProvider,
    // SearchuserPage,
    Camera,
    ChatInfoProvider,
    BarcodeScanner,
    LinkedIn,
    InAppBrowser,
    HTTP,
    // Slides,
    // ViewChild
  ]
})
export class AppModule {}

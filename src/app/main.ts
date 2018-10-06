import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app.module';
import {HTTP} from '@ionic-native/http';
platformBrowserDynamic().bootstrapModule(AppModule);
HTTP.getPluginRef = () => "cordova.plugin.http";

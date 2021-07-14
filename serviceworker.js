var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/css/estilos.css',
    '/galeria/',
    '/formulario/',
    '/registro/',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {

          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
          
        })
    );
});


//////////////////////////////////////////////////////////
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');


var firebaseConfig = {
  apiKey: "AIzaSyB9oXa4NGHrjEtcql_UFC4x-ZFKiPpnPOU",
  authDomain: "djangoryomakween.firebaseapp.com",
  projectId: "djangoryomakween",
  storageBucket: "djangoryomakween.appspot.com",
  messagingSenderId: "885179350380",
  appId: "1:885179350380:web:04ec1da888ea51ffe38749"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

////////////////////////////////////////////////////////////
let messaging = firebase.messaging();
/////////////// modelo de notificacion offline ////////////
messaging.setBackgroundMessageHandler(function(payload) {
    let titulo = 'Titulo'
    let opciones = {
        body: 'Cuerpo de Notificacion',
        icon: '/static/img/icon.png'
    }
    self.registration.showNotification(titulo, opciones)
});
////////////////////////////////////////////////////////////


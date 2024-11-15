import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );


const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const controls = new OrbitControls( camera, renderer.domElement );

//controls.update() must be called after any manual changes to the camera's transform
camera.position.set( 0, 20, 100 );
controls.update();


const earthTexture= new THREE.TextureLoader().load('2k_earth_daymap.jpg')

const geometry = new THREE.SphereGeometry(2,32,32);
const material = new THREE.MeshBasicMaterial( { map:earthTexture} );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );


camera.position.set(0,0,5);

function animate() {
    requestAnimationFrame(animate);
    if (false) {cube.rotation.y+=0.025;}
    controls.update();
	renderer.render( scene, camera );
}
animate();

document.addEventListener('keydown',function(event){
    var code = event.keyCode;
    if (code == 37) cube.rotation.y -=0.1;
    if (code == 38) cube.rotation.x -=0.1;
    if (code == 39) cube.rotation.y +=0.1;
    if (code == 40) cube.rotation.x +=0.1;
});







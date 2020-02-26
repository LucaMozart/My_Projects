import React, {Component} from 'react';
import {StyleSheet, View, Image, ScrollView, TouchableOpacity, Text,} from 'react-native';


export default class Menu extends Component {
	render() {
		return (
			<ScrollView style={styles.container}>
				
				<View style={styles.inner}>

					<Image style={styles.image2} source={require('../images/testing.jpg')}/>
				</View>
			</ScrollView>
		);
	}
}

const styles = StyleSheet.create({
  container: {
  	flex: 1,
  	backgroundColor: '#FCFFFA',
  },

  form: {
  	justifyContent: 'center', 
	alignItems: 'center',
	flexGrow: 1 

  },  	

  inner: {
  	marginTop : 0,

	alignItems: 'center',
	flexGrow: 1, 
	justifyContent: 'center',

  },

  image: {
  	width:  '90%', 
  	height: 110,
  },
   image2: {
   	marginTop : 200,
  	width:  200, 
  	height: 200,
  },

  container2: {
    marginTop: 'center',
	flex: 1,
	justifyContent: 'center',
	paddingHorizontal: 10

  },

  button: {
  	borderWidth: 0,
  	borderColor: 'black',
  	width:  100, 
  	height: 100,
    borderRadius: 0,
    backgroundColor: '#FCFFFA',
    padding: 10
  },
  menu: {
	borderWidth: 2,
  	justifyContent: 'center',
  	width:  140, 
  	height: 50,
    borderRadius: 0,
    backgroundColor: '#FCFFFA',
    padding: 10
  },
  fonte:{
  	fontSize: 20,
  	color: 'black',
  },
});
Menu.navigationOptions = {
    header: null,
};

import React, {Component} from 'react';
import {StyleSheet, View, Image, ScrollView, TouchableOpacity, Text, Alert} from 'react-native';
import Produto from './Produto';
import { createStackNavigator, createAppContainer } from 'react-navigation'; // Version can be specified in package.json

export default class Papel extends Component {

    constructor(props) {
      super(props);
      this.state = { id: 'id'};
      const {id} = this.state;
      const {image} = this.state;
  }

  Papel00(id) {
    let imagePath = require('../images/papel00.jpg');
    this.state.id = id;
    this.state.image = imagePath;
            this.props.navigation.navigate('Tela5', {
              itemId: 'Move Your Wall',
              Imagem: this.state.image,
              Sobre: 'Papel de parede geométrico colorido.',
            });
    this.props.navigation.navigate('Tela5');

  } 

    Papel01(id) {
    let imagePath = require('../images/papel01.jpg');
    this.state.id = id;
    this.state.image = imagePath;
            this.props.navigation.navigate('Tela5', {
              itemId: 'Move Your Wall',
              Imagem: this.state.image,
              Sobre: 'Papel de parede geométrico, 3D, branco com bage.',
            });
    this.props.navigation.navigate('Tela5');

  } 

    Papel02(id) {
    let imagePath = require('../images/papel02.jpg');
    this.state.id = id;
    this.state.image = imagePath;
            this.props.navigation.navigate('Tela5', {
              itemId: 'Move Your Wall',
              Imagem: this.state.image,
              Sobre: 'Papel de parede geométrico azul, 3D, rosa e amarelo.',
            });
    this.props.navigation.navigate('Tela5');

  }         

    Papel03(id) {
    let imagePath = require('../images/papel03.jpg');
    this.state.id = id;
    this.state.image = imagePath;
            this.props.navigation.navigate('Tela5', {
              itemId: 'Move Your Wall',
              Imagem: this.state.image,
              Sobre: 'Papel de parede geométrico, 3D, marrom.',
            });
    this.props.navigation.navigate('Tela5');

  }         



	render() {
		return (
			<ScrollView style={styles.container}>
				<View style={styles.inner}>
					<Image style={styles.image0} source={require('../images/arthouselogo.jpg')}/>
					<Text style={styles.fonte}> Papel de Parede </Text>
				</View>

				<View style={styles.container1} >
					<View style={styles.itens}>
                		<TouchableOpacity placeholder='id' style={styles.menu} onPress={() => this.Papel00('00')} >
                      		<Image style={styles.image} source={require('../images/papel00.jpg')} />
                		</TouchableOpacity>
                	</View>

                	<View style={styles.itens}>
                		<TouchableOpacity style={styles.menu} onPress={() => this.Papel01('01')} >
                      		<Image style={styles.image} source={require('../images/papel01.jpg')} />
                		</TouchableOpacity>
                	</View>

                	<View style={styles.itens}>
                		<TouchableOpacity style={styles.menu} onPress={() => this.Papel02('02')} >
                      		<Image style={styles.image} source={require('../images/papel02.jpg')} />
                		</TouchableOpacity>
                	</View>

                	<View style={styles.itens}>
                		<TouchableOpacity style={styles.menu} onPress={() => this.Papel03('03')} >
                      		<Image style={styles.image} source={require('../images/papel03.jpg')} />
                		</TouchableOpacity>
                	</View>
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

  container1: {
    flexDirection: 'row',
    flexWrap: 'wrap',
},
  inner: {
  	marginTop : 0,
	  alignItems: 'center',
  	flexGrow: 1, 
    justifyContent: 'center',
  },

  image0: {
  	width:  300, 
  	height: 102,
  },

  fonte:{
    fontSize: 30,
    color: 'white',
    backgroundColor: 'rgba(30, 30, 30, 0.5)',
    borderRadius: 20,
    marginTop: 5,
  },

    itens: {
        width: 205,
        height: 220,
  },

    menu: {
        borderWidth: 0,
        width:  '100%', 
        height: '100%',
        borderRadius: 0,
        backgroundColor: '#FCFFFA',
        padding: 10
  },

    image: {
        width:  '100%', 
        height: '100%',
        position: 'relative',
  },
    fonte2:{
        fontSize: 30,
        color: 'black',
        position: 'absolute',
        bottom: 170,
        left: 80,
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        borderRadius: 7,

  },


});

Papel.navigationOptions = {
    header: null,
};

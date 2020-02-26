import React, {Component} from 'react';
import {StyleSheet, View, Image, ScrollView, TouchableOpacity, Text, Alert} from 'react-native';
import Produto from './Produto';
import { createStackNavigator, createAppContainer } from 'react-navigation'; // Version can be specified in package.json

export default class Painel extends Component {

    constructor(props) {
      super(props);
      this.state = { id: 'id'};
      const {id} = this.state;
      const {image} = this.state;
  }

  Painel00(id) {
    let imagePath = require('../images/painel00.jpg');
    this.state.id = id;
    this.state.image = imagePath;
            this.props.navigation.navigate('Tela5', {
              itemId: 'Paisagem',
              Imagem: this.state.image,
              Sobre: 'Painel fotográfico de paisagem, fazemos tamanho e imagem personalizada.',
            });
    this.props.navigation.navigate('Tela5');

  } 

    Painel01(id) {
    let imagePath = require('../images/painel01.jpg');
    this.state.id = id;
    this.state.image = imagePath;
            this.props.navigation.navigate('Tela5', {
              itemId: 'Homem Aranha',
              Imagem: this.state.image,
              Sobre: 'Painel fotográfico de Homem Aranha, fazemos tamanho e imagem personalizada.',
            });
    this.props.navigation.navigate('Tela5');

  } 

    Painel02(id) {
    let imagePath = require('../images/painel02.jpg');
    this.state.id = id;
    this.state.image = imagePath;
            this.props.navigation.navigate('Tela5', {
              itemId: 'Os Vingadores',
              Imagem: this.state.image,
              Sobre: 'Painel fotográfico dos vingadores, fazemos tamanho e imagem personalizada.',
            });
    this.props.navigation.navigate('Tela5');

  }         

    Painel03(id) {
    let imagePath = require('../images/painel03.jpg');
    this.state.id = id;
    this.state.image = imagePath;
            this.props.navigation.navigate('Tela5', {
              itemId: 'Deadpool',
              Imagem: this.state.image,
              Sobre: 'Painel fotográfico do Deadpool, fazemos tamanho e imagem personalizada.',
            });
    this.props.navigation.navigate('Tela5');

  }         



	render() {
		return (
			<ScrollView style={styles.container}>
				<View style={styles.inner}>
					<Image style={styles.image0} source={require('../images/arthouselogo.jpg')}/>
					<Text style={styles.fonte}> Painel Fotográfico </Text>
				</View>

				<View style={styles.container1} >
					<View style={styles.itens}>
                		<TouchableOpacity placeholder='id' style={styles.menu} onPress={() => this.Painel00('00')} >
                      		<Image style={styles.image} source={require('../images/painel00.jpg')} />
                		</TouchableOpacity>
                	</View>

                	<View style={styles.itens}>
                		<TouchableOpacity style={styles.menu} onPress={() => this.Painel01('01')} >
                      		<Image style={styles.image} source={require('../images/painel01.jpg')} />
                		</TouchableOpacity>
                	</View>

                	<View style={styles.itens}>
                		<TouchableOpacity style={styles.menu} onPress={() => this.Painel02('02')} >
                      		<Image style={styles.image} source={require('../images/painel02.jpg')} />
                		</TouchableOpacity>
                	</View>

                	<View style={styles.itens}>
                		<TouchableOpacity style={styles.menu} onPress={() => this.Painel03('03')} >
                      		<Image style={styles.image} source={require('../images/painel03.jpg')} />
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

Painel.navigationOptions = {
    header: null,
};

import React, {Component} from 'react';
import {StyleSheet, View, Image, ScrollView, TouchableOpacity, Text, Alert, Button} from 'react-native';
import Papel from './Papel';
import { createStackNavigator, createAppContainer } from 'react-navigation'; // Version can be specified in package.json

export default class Produto extends Component {
      constructor(props) {
      super(props);
      this.state = { id: '', imagem:''};
  }

  onPressButton() {
    Alert.alert('Botão em desenvolvimento')
  }

	render() {
    const { navigation } = this.props;
    const itemId = navigation.getParam('itemId', 'NO-ID');
    const Imagem = navigation.getParam('Imagem', 'No-IMAG');
    const Sobre = navigation.getParam('Sobre', 'NO-INF');
    this.state.imagem = JSON.stringify(Imagem)
    var image = this.state.imagem;
    let imagePath = require("../images/arthouselogo.jpg");
		return (
      <ScrollView style={styles.container}>
        <View style={styles.inner}>
          <Image style={styles.image0}  source={require('../images/arthouselogo.jpg')} />
          </View>
          <View style={styles.itensT}>
          <Text style={styles.fonte}>{JSON.stringify(itemId)}</Text>
          </View>
          <View style={styles.itens}>
          <Image style={styles.image1} source={image} />
          </View>
          <View style={styles.itensText}>
          <Text style={styles.fonteSobre}>{JSON.stringify(Sobre)}</Text>
          </View>
          <View style={styles.viewbuttom}>
              <TouchableOpacity style={styles.buttom} onPress={() => this.onPressButton()}>
                      <Text style={styles.fonteButtom} >COMPRAR</Text>
              </TouchableOpacity>
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
      itens: {
        width: '100%',
        height: 400,
  },
      itensText: {
        alignItems: 'center',
        width: '100%',
        height: 75,
        backgroundColor: '#FFFFB5',

  },
      itensT: {
        marginTop: 20,
        alignItems: 'center',
        width: '100%',
        height: 50,
        backgroundColor: '#FFFFB5',

  },
      viewbuttom: {
        alignItems: 'center',
        width: '100%',
        height: 50,
        justifyContent: 'center',

  },
  inner: {
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
    color: 'black',
    marginTop: 5,
  },
    fonteSobre:{
      fontSize: 18,
      color: 'black',
      marginTop: 5,
  },
    image1: {
      width:  '100%', 
      height: '100%',
      position: 'relative',
  },
      buttom: {
        borderWidth: 0,
        width:  '100%', 
        height: 50,
        borderRadius: 0,
        backgroundColor: '#FFDA2E',
        padding: 10
  },
    fonteButtom:{
      fontSize: 20,
      color: 'black',
              left: 140,


  },


});
Produto.navigationOptions = {
    header: null,
};

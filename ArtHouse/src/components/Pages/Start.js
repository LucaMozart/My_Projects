import React, {Component} from 'react';
import {StyleSheet, View, Image, ScrollView, TouchableOpacity, Text, Alert} from 'react-native';



export default class Start extends Component {
    onPressButton() {
    Alert.alert('Botão em desenvolvimento')
  }
	render() {
		return (
			<ScrollView style={styles.container}>
				<View style={styles.inner}>
					<Image style={styles.image0} source={require('../images/arthouselogo.jpg')}/>
				</View>

        <View style={styles.container2} >
              <View style={styles.itens}>
              <TouchableOpacity style={styles.menu} onPress={() => this.props.navigation.navigate('Tela4')}>
                      <Image style={styles.image} source={require('../images/papel00.jpg')} />
                      <Text style={styles.fonte} >Papel de Parede</Text>
              </TouchableOpacity>
              </View>
              <View style={styles.itens}>
              <TouchableOpacity style={styles.menu} onPress={() => this.props.navigation.navigate('Tela8')}>
                      <Image style={styles.image} source={require('../images/painel00.jpg')}/>
                      <Text style={styles.fonte} >Painel Fotográfico</Text>
              </TouchableOpacity>
              </View>
              <View style={styles.itens}>
              <TouchableOpacity style={styles.menu} onPress={() => this.onPressButton()}>
                      <Image style={styles.image} source={require('../images/envelopamento.jpg')}/>
                      <Text style={styles.fonte} >Envelopamento</Text>
              </TouchableOpacity>
              </View>
              <View style={styles.itens}>
              <TouchableOpacity style={styles.menu} onPress={() => this.onPressButton()}>
                      <Image style={styles.image} source={require('../images/sanca.jpg')}/>
                      <Text style={styles.fonte} >Sanca Sintética</Text>
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

  inner: {
  	marginTop : 0,
    flexDirection: 'row',
	  alignItems: 'center',
	  flexGrow: 1, 
	  justifyContent: 'center',
  },

  image0: {
  	width:  300, 
  	height: 102,
  },

  container2: {
    flexDirection: 'row',
    flexWrap: 'wrap',

  },
  itens: {
        width: '100%',
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

    fonte:{
        fontSize: 30,
        color: 'black',
        position: 'absolute',
        bottom: 170,
        left: 80,
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        borderRadius: 7,

  },


});
Start.navigationOptions = {
    header: null,
};


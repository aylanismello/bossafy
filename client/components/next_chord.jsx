import React from 'react';
import { Reveal, Segment, Image, Button } from 'semantic-ui-react';

const NextChord = ({ chord, currentChord, fetchNextChordAgain }) => (
	<Segment>
		<h1>Next Chord for {currentChord}</h1>
		<h2>{chord.name}</h2>
		<h3> {chord.tab} </h3>
		<Button basic color="teal" onClick={() => fetchNextChordAgain()}>
			Try Again
		</Button>
	</Segment>
);

export default NextChord;

import React from 'react';
import { Table, Popup } from 'semantic-ui-react';

const rootNotes = [
	'Ab',
	'A',
	'Bb',
	'B',
	'C',
	'Db',
	'D',
	'Eb',
	'E',
	'F',
	'F#',
	'G'
];

const Row = ({ chordType, chordDict, fetchNextChord }) => {
	return (
		<Table.Row>
			{rootNotes.map(rootNote => {
				const fullChord = `${rootNote}${chordType}`;
				const chordTab = chordDict[fullChord] || 'wUt';
				return (
					<Table.Cell onClick={() => fetchNextChord(fullChord)} className='chord-cell'>
						<Popup trigger={<div> {fullChord}</div>} content={chordTab} />
					</Table.Cell>
				);
			})}
		</Table.Row>
	);
};

const ChordsTable = ({ chords, chordDict, fetchNextChord }) => (
	<Table celled collapsing sortable color="teal" textAlign="center" columns="12">
		<Table.Header>
			<Table.Row>
				{rootNotes.map(rootNote => (
					<Table.HeaderCell>{rootNote} Chords</Table.HeaderCell>
				))}
			</Table.Row>
		</Table.Header>

		<Table.Body>
			{Object.keys(chords).map(chordType => (
				<Row chordType={chordType} chordDict={chordDict} fetchNextChord={fetchNextChord} />
			))}

		</Table.Body>
	</Table>
);

export default ChordsTable;

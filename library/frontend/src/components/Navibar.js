import Container from 'react-bootstrap/Container';
import { Nav, Navbar, Button} from 'react-bootstrap';
import '../App.css';

function Navibar() {
  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">Navbar</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Users</Nav.Link>
            <Nav.Link href="#pricing">About</Nav.Link>
          </Nav>
          <Nav>
            <Button variant='primary' className='margin-right'>Log In</Button>
            <Button variant='secondary' className='margin-right'>Sign out</Button>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default Navibar;

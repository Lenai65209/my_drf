import Container from 'react-bootstrap/Container';
import { Nav, Navbar, Button} from 'react-bootstrap';
import '../App.css';

function Navibar() {
  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/">Navbar</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="Users">Users</Nav.Link>
            <Nav.Link href="About">About</Nav.Link>
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

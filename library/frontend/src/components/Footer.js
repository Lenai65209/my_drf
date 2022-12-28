import Card from 'react-bootstrap/Card';
import { Nav, Navbar, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'
import '../App.css';

function Footer() {
  return (
  <nav class="navbar fixed-bottom navbar-expand-lg navbar-green my-width">
    <Card className=" card text-center my-width">
      <Card.Header>Featured</Card.Header>
      <Card.Body>
        <Card.Title>Special title treatment</Card.Title>
        <Card.Text>
          With supporting text below as a natural lead-in to additional content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
      <Card.Footer className="text-muted">&copy; Все права защищены</Card.Footer>
    </Card>
  </nav>
  );
}

export default Footer;